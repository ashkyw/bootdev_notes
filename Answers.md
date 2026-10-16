Refactor in progress:
```m
let
    // Valid column types
    ColumnTypeRecords = [
        Text = type text,
        Number = type number,
        Float = Int64.Type,
        Date = type date,
        Time = type time,
        DateTime = type datetime,
        Bool = type logical
    ],
    
    // Valid delimiters
    DelimiterRecords = [
        semi = ";",
        colon = ":",
        fslash = "/",
        bslash = "\",
        comma = ","
    ],
    
    // Validate Record
    fnIsValidRecord = (validRecord as record, value as any) as logical =>
        List.Contains(Record.FieldValues(validRecord), value),
    
    // Trim, Split list at delimiter 
    fnCleanSplitAndFilterList = (listColumn as nullable text, delimiter as text) as list =>
        let
            isValidDelimiter = fnIsValidRecord(DelimiterRecords, delimiter),
            cleanedAndSplit = 
                if listColumn = null or listColumn = "" then {}
                else if not isValidDelimiter then
                    error "Invalid delimiter: '" & delimiter & "'. Must be one of: " & Text.Combine(Record.FieldValues(DelimiterRecords), " ")
                else 
                    List.Transform(Text.Split(Text.Trim(listColumn), delimiter), Text.Trim),
            filtered = List.Select(cleanedAndSplit, each _ <> "")
        in
            filtered,
    
    // Apply Type to selected columns
    fnApplyColumnType = (table as table, columnList as list, validItem as text) as table =>
        let
            targetType = Record.Field(ColumnTypeRecords, validItem),
            columnTypePairs = List.Transform(columnList, each {_, targetType})
        in
            Table.TransformColumnTypes(table, columnTypePairs),
    
    // Load file
    fnLoadFile = (path as text, file as text, extension as text, fileNameDelimiter as text) =>
        let
            // Get all files from path
            FilesRaw = Folder.Contents(path),

            // Keep only real files
            Files = Table.SelectRows(
                FilesRaw,
                each [Content] <> null and [Extension] <> null
            ),

            FilePrefix = Text.Trim(Text.BeforeDelimiter(file, fileNameDelimiter)),

            Filtered = Table.SelectRows(
                Files, 
                each 
                    Text.Contains([Name], FilePrefix)
                    and Text.EndsWith([Name], FileExtension)
                    and not Text.Contains([Name], FileNameDelimiter)
                ),

            Sorted =
                if Table.HasColumns(Filtered, "Date modified")
                then Table.Sort(Filtered, {{"Date modified", Order.Descending}})
                else if Table.HasColumns(Filtered, "DateCreated")
                then Table.Sort(Filtered, {{"DateCreated", Order.Descending}})
                else Filtered,

            Latest =
                if Table.RowCount(Sorted)=0 then null else Sorted{0},

            LatestPath =
                if Latest=null then null else Latest[Folder Path] & Latest[Name],

            
                    // If no file → log error
                    FileResult =
                        if LatestPath=null then
                            [
                                Data = null,
                                Diagnostics = 
                                [
                                    FilePath="(none)",
                                    Error="No matching file",
                                    RequestedColumns=WantedColumns,
                                    MatchedColumns={},
                                    MissingColumns=WantedColumns
                                ]
                            ]
                        else
                            FileFunction(LatestPath, Sheet, WantedColumns),

                    TableData   = FileResult[Data],
                    Diagnostics = FileResult[Diagnostics]

    in
        [
            Data = TableData,
            Diagnostics = Diagnostics
        ],


    fnCreateNewTable = (table as table) =>
        let 
            TableResults = Table.AddColumn(table, "Results", each
            let
                Path                  = [FolderPath],
                File                  = [FileName],
                Sheet                 = [SheetName],
                FileNameDelimiter     = Text.Lower([FileDelimiter]),
                FileExtension         = Text.Lower([FileExtension]),
                RawTextCols           = fnCleanSplitAndFilterList([TextColumns], [SplitDelimiter]),               
                RawIntCols            = fnCleanSplitAndFilterList([NumberColumns], [SplitDelimiter]),
                RawFloatCols          = fnCleanSplitAndFilterList([DecimalColumns], [SplitDelimiter]),
                TextCols              = fnApplyColumnType(RawTextCols, )
                IntCols               =
                FloatCols             =
                WantedColumns         = List.Combine({TextCols, IntCols, FloatCols})
            in
                WantedColumns
            )
        in
            TableResults

in 
    [
        ColumnTypes = ColumnTypeRecords,
        Delimiters = DelimiterRecords,
        ValidRecord = fnIsValidRecord,
        FilteredList = fnCleanSplitAndFilterList,
        AppliedColumnTypes = fnApplyColumnType
    ]
/*
        // Load each file defined in ConfigTable
        AddResults = Table.AddColumn(ConfigTable, "Results", each
            let
                FolderPath            = [FolderPath],
                Pattern               = [FileName],
                Sheet                 = [SheetName],
                EndingDelimiter       = Text.Lower([FileDelimiter]),
                FileExtension         = Text.Lower([FileExtension]),
                TextCols              = fnSplitText([TextColumns], [SplitDelimiter]),               
                IntCols               = ParseList([NumberColumns], [SplitDelimiter]),
                FloatCols             = ParseList([DecimalColumns], [SplitDelimiter]),
                WantedColumns         = List.Combine({TextCols, IntCols, FloatCols}),


        // Locate newest matching file (NON-RECURSIVE, CORRECTED)
        FilesRaw = Folder.Contents(FolderPath),

        // keep only real files
        Files = Table.SelectRows(
            FilesRaw,
            each [Content] <> null and [Extension] <> null
        ),

        FilePrefix = Text.Trim(
            Text.BeforeDelimiter(Pattern, EndingDelimiter)
            ),
    

        Filtered = Table.SelectRows(
            Files, 
            each 
                Text.Contains([Name], FilePrefix)
                and Text.EndsWith([Name], FileExtension)
                and not Text.Contains([Name], EndingDelimiter)
            ),

        Sorted =
            if Table.HasColumns(Filtered, "Date modified")
            then Table.Sort(Filtered, {{"Date modified", Order.Descending}})
            else if Table.HasColumns(Filtered, "DateCreated")
            then Table.Sort(Filtered, {{"DateCreated", Order.Descending}})
            else Filtered,

        Latest =
            if Table.RowCount(Sorted)=0 then null else Sorted{0},

        LatestPath =
            if Latest=null then null else Latest[Folder Path] & Latest[Name],

        
                // If no file → log error
                FileResult =
                    if LatestPath=null then
                        [
                            Data = null,
                            Diagnostics = 
                            [
                                FilePath="(none)",
                                Error="No matching file",
                                RequestedColumns=WantedColumns,
                                MatchedColumns={},
                                MissingColumns=WantedColumns
                            ]
                        ]
                    else
                        FileFunction(LatestPath, Sheet, WantedColumns),

                TableData   = FileResult[Data],
                Diagnostics = FileResult[Diagnostics]

            in
                [
                    Data = TableData,
                    Diagnostics = Diagnostics
                ]
        ),


        // Expand diagnostics
        Expanded = Table.ExpandRecordColumn(AddResults, "Results", {"Data", "Diagnostics"}),


        // Master diagnostic table
        Log =
            if List.Count(List.RemoveNulls(Expanded[Diagnostics])) > 0 then
                Table.Combine(List.Transform(Expanded[Diagnostics], each Table.FromRecords({_})))
            else
                #table({}, {}),


        // Combine loaded datasets
        Valid = Table.SelectRows(Expanded, each [Data] <> null),

        Combined =
            if Table.RowCount(Valid)=0 then #table({}, {})
            else Table.Combine(Valid[Data])
    in
        [
            Data = Combined,
            Log = Log
        ]
in
    parse_configtable
*/
```

Original:

```m
let
    MPM_configtable = (ConfigTable as table, FileFunction as function) =>
    let
        //-----------------------------------------------------------
        // Helper: semicolon-splitter
        //-----------------------------------------------------------
        SplitSemi = (txt as nullable text) as list =>
            let
                cleaned = if txt=null then "" else Text.Trim(txt),
                split = if cleaned="" then {} else List.Transform(Text.Split(cleaned, ";"), Text.Trim),
                nonBlank = List.Select(split, each _ <> "")
            in
                nonBlank,

        //-----------------------------------------------------------
        // Load each file defined in ConfigTable
        //-----------------------------------------------------------
        AddResults = Table.AddColumn(ConfigTable, "Results", each
            let
                FolderPath = [FolderPath],
                Pattern    = [FilePattern],
                Sheet      = [SheetName],
                AreaVal    = [Area],
                ModelVal   = [Model],

                // Column lists
                StandardCols = SplitSemi([StandardColumns]),
                KatashikiCols =
                    if [KatashikiColumns] = null or [KatashikiColumns] = ""
                    then {}
                    else SplitSemi([KatashikiColumns]),

                WantedColumns = List.Combine({StandardCols, KatashikiCols}),

        //-----------------------------------------------------------
        // Locate newest matching file (NON-RECURSIVE, CORRECTED)
        //-----------------------------------------------------------
        FilesRaw = Folder.Contents(FolderPath),

        // keep only real files
        Files = Table.SelectRows(
            FilesRaw,
            each [Content] <> null and [Extension] <> null
        ),

        Prefix = Text.BeforeDelimiter(Pattern, "*"),

        Filtered = Table.SelectRows(Files, each Text.StartsWith([Name], Prefix)),

        Sorted =
            if Table.HasColumns(Filtered, "Date modified")
            then Table.Sort(Filtered, {{"Date modified", Order.Descending}})
            else if Table.HasColumns(Filtered, "DateCreated")
            then Table.Sort(Filtered, {{"DateCreated", Order.Descending}})
            else Filtered,

        Latest =
            if Table.RowCount(Sorted)=0 then null else Sorted{0},

        LatestPath =
            if Latest=null then null else Latest[Folder Path] & Latest[Name],

                //-----------------------------------------------------------
                // If no file → log error
                //-----------------------------------------------------------
                FileResult =
                    if LatestPath=null then
                        [
                            Data = null,
                            Diagnostics = 
                            [
                                FilePath="(none)",
                                Error="No matching file",
                                RequestedColumns=WantedColumns,
                                MatchedColumns={},
                                MissingColumns=WantedColumns
                            ]
                        ]
                    else
                        FileFunction(LatestPath, Sheet, WantedColumns),

                TableData   = FileResult[Data],
                Diagnostics = FileResult[Diagnostics],

                //-----------------------------------------------------------
                // Add Area + Model fields
                //-----------------------------------------------------------
                WithMeta =
                    if TableData=null then null else
                        Table.AddColumn(
                            Table.AddColumn(TableData, "Area", each AreaVal, type text),
                            "Model", each ModelVal, type text
                        )
            in
                [
                    Data = WithMeta,
                    Diagnostics = Diagnostics
                ]
        ),

        //-----------------------------------------------------------
        // Expand diagnostics
        //-----------------------------------------------------------
        Expanded = Table.ExpandRecordColumn(AddResults, "Results", {"Data", "Diagnostics"}),

        //-----------------------------------------------------------
        // Master diagnostic table
        //-----------------------------------------------------------
        Log =
            if List.Count(List.RemoveNulls(Expanded[Diagnostics])) > 0 then
                Table.Combine(List.Transform(Expanded[Diagnostics], each Table.FromRecords({_})))
            else
                #table({}, {}),

        //-----------------------------------------------------------
        // Combine loaded datasets
        //-----------------------------------------------------------
        Valid = Table.SelectRows(Expanded, each [Data] <> null),

        Combined =
            if Table.RowCount(Valid)=0 then #table({}, {})
            else Table.Combine(Valid[Data]),

        //-----------------------------------------------------------
        // FULL CLEANING PIPELINE — RESTORED
        //-----------------------------------------------------------

        // 1: Replace Excel errors → null
        CleanErrors = Table.TransformColumns(
            Combined,
            List.Transform(Table.ColumnNames(Combined), each {_, (x)=> try x otherwise null})
        ),

        // 2: Convert all to text
        AsText = Table.TransformColumnTypes(
            CleanErrors,
            List.Transform(Table.ColumnNames(CleanErrors), each {_, type text})
        ),

        // 3: Replace nulls with blanks
        NoNulls = Table.TransformColumns(
            AsText,
            List.Transform(Table.ColumnNames(AsText), each {_, each if _=null then "" else _, type text})
        ),

        // 4: Convert quantity safely
        QtyInt = Table.TransformColumns(
            NoNulls,
            {{"Quantity per Vehicle",
                each if _="" then null else Number.FromText(_),
                Int64.Type
            }}
        ),

        // 5: Replace null quantity with 0
        QtyFilled = Table.ReplaceValue(
            QtyInt, null, 0, Replacer.ReplaceValue, {"Quantity per Vehicle"}
        ),

        // 6: Build normalized 12-digit part number
        With12 = Table.AddColumn(
            QtyFilled,
            "12-Digit",
            each Text.Combine({
                Text.From([First Five],""),
                Text.From([Last Five],""),
                Text.From([Last Two],"")
            }),
            type text
        ),

        // 7: Filter invalid part numbers
        Filtered = Table.SelectRows(
            With12,
            each not List.Contains({"", null, "1", "*", " "}, [#"First Five"])
        )

    in
        [
            Data = Filtered,
            Log = Log
        ]
in
    MPM_configtable
```
