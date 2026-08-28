Currently used vuteq_file_data
```m
let
    get_vuteq_file_data = (fileContent as binary, filePath as text, sheetName as text, columnsToKeep as list) as record =>
    let
        //-----------------------------------------------------------
        // Load Excel file from binary content
        //-----------------------------------------------------------
        SourceTry = try Excel.Workbook(fileContent, null, true),

        Source =
            if SourceTry[HasError] then
                error "Failed to load file: " & filePath & " | " & SourceTry[Error][Message]
            else
                SourceTry[Value],

        //-----------------------------------------------------------
        // Validate sheet exists
        //-----------------------------------------------------------
        SheetRows = Table.SelectRows(Source, each [Name] = sheetName),

        Sheet =
            if Table.RowCount(SheetRows) = 0 then
                error "Sheet '" & sheetName & "' not found in " & filePath
            else
                SheetRows{0},

        Kind = Sheet[Kind],

        Raw =
            if Kind = "Sheet" or Kind = "Worksheet" then Sheet[Data]
            else error "Unsupported Excel object type: " & Kind,

        //-----------------------------------------------------------
        // Convert to table + promote headers
        //-----------------------------------------------------------
        AsTable =
            if Value.Is(Raw, type table)
            then Raw
            else Table.FromList(Raw, Splitter.SplitByNothing(), {"Column1"}),

        Promoted = Table.PromoteHeaders(AsTable, [PromoteAllScalars=true]),

        // Normalize headers by removing invisible Unicode characters
        NormalizeHeaders = Table.TransformColumnNames(
            Promoted,
            each Text.Clean(Text.Select(_, each Character.ToNumber(_) <> 8203))
        ),

        //-----------------------------------------------------------
        // NORMALIZE FIRST 3 MERGED HEADER COLUMNS
        //-----------------------------------------------------------
        MergedFix =
            let
                cn = Table.ColumnNames(Promoted),
                ren1 = Table.RenameColumns(Promoted, {{cn{0}, "First Five"}}, MissingField.Ignore),
                ren2 = Table.RenameColumns(ren1, {{cn{1}, "Last Five"}}, MissingField.Ignore),
                ren3 = Table.RenameColumns(ren2, {{cn{2}, "Last Two"}}, MissingField.Ignore),
                ren4 = Table.RenameColumns(ren3, {{cn{3}, "Old First Five"}}, MissingField.Ignore),
                ren5 = Table.RenameColumns(ren4, {{cn{4}, "Old Last Five"}}, MissingField.Ignore),
                ren6 = Table.RenameColumns(ren5, {{cn{5}, "Old Last Two"}}, MissingField.Ignore)
            in
                ren6,

        //-----------------------------------------------------------
        // Match requested column names
        //-----------------------------------------------------------
        Available = Table.ColumnNames(MergedFix),
        Matched = List.Select(columnsToKeep, each List.Contains(Available, _)),
        Missing = List.Difference(columnsToKeep, Matched),

        Extracted = try Table.SelectColumns(MergedFix, Matched, MissingField.UseNull)
                    otherwise MergedFix,

        //-----------------------------------------------------------
        // Diagnostics record
        //-----------------------------------------------------------
        Diagnostics =
            [
                FilePath = filePath,
                SheetName = sheetName,
                RequestedColumns = columnsToKeep,
                MatchedColumns = Matched,
                MissingColumns = Missing,
                RowCount = Table.RowCount(Extracted)
            ]
    in
        [
            Data = Extracted,
            Diagnostics = Diagnostics
        ]
in
    get_vuteq_file_data
```

New sharpoint_file_data:
```m
let
    get_sharepoint_file_data = (fileContent as binary, filePath as text, sheetName as text, columnsToKeep as list) as record =>
    let
        //-----------------------------------------------------------
        // Load Excel file from binary content
        //-----------------------------------------------------------
        SourceTry = try Excel.Workbook(fileContent, null, true),

        Source =
            if SourceTry[HasError] then
                error "Failed to load file: " & filePath & " | " & SourceTry[Error][Message]
            else
                SourceTry[Value],

        //-----------------------------------------------------------
        // Validate sheet exists
        //-----------------------------------------------------------
        SheetRows = Table.SelectRows(Source, each [Name] = sheetName),

        Sheet =
            if Table.RowCount(SheetRows) = 0 then
                error "Sheet '" & sheetName & "' not found in " & filePath
            else
                SheetRows{0},

        Kind = Sheet[Kind],

        Raw =
            if Kind = "Sheet" or Kind = "Worksheet" then Sheet[Data]
            else error "Unsupported Excel object type: " & Kind,

        //-----------------------------------------------------------
        // Convert to table + promote headers
        //-----------------------------------------------------------
        AsTable =
            if Value.Is(Raw, type table)
            then Raw
            else Table.FromList(Raw, Splitter.SplitByNothing(), {"Column1"}),

        Promoted = Table.PromoteHeaders(AsTable, [PromoteAllScalars=true]),

        // Normalize headers by removing invisible Unicode characters
        NormalizeHeaders = Table.TransformColumnNames(
            Promoted,
            each Text.Clean(Text.Select(_, each Character.ToNumber(_) <> 8203))
        ),

        //-----------------------------------------------------------
        // Match requested column names
        //-----------------------------------------------------------
        Available = Table.ColumnNames(NormalizeHeaders),
        Matched = List.Select(columnsToKeep, each List.Contains(Available, _)),
        Missing = List.Difference(columnsToKeep, Matched),

        Extracted = try Table.SelectColumns(NormalizeHeaders, Matched, MissingField.UseNull)
                    otherwise NormalizeHeaders,

        //-----------------------------------------------------------
        // Diagnostics record
        //-----------------------------------------------------------
        Diagnostics =
            [
                FilePath = filePath,
                SheetName = sheetName,
                RequestedColumns = columnsToKeep,
                MatchedColumns = Matched,
                MissingColumns = Missing,
                RowCount = Table.RowCount(Extracted)
            ]
    in
        [
            Data = Extracted,
            Diagnostics = Diagnostics
        ]
in
    get_sharepoint_file_data
```

Previous vuteq_mpm_configtable:
```m
let
    vuteq_configtable = (ConfigTable as table, FileFunction as function) =>
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
                SiteUrl    = [SiteUrl],
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
            // Locate newest matching file from SharePoint
            //-----------------------------------------------------------
            AllFiles = SharePoint.Files(SiteUrl, [ApiVersion = 15]),

            // Filter to target folder (full URL match)
            InFolder = Table.SelectRows(AllFiles, each 
                Text.Contains([Folder Path], FolderPath)
            ),

            // Filter by file name pattern (wildcard support)
            Prefix = Text.Trim(Text.BeforeDelimiter(Pattern, "*")),
            Suffix = Text.Trim(Text.AfterDelimiter(Pattern, "*")),

            Filtered = Table.SelectRows(InFolder, each 
                Text.StartsWith([Name], Prefix) 
                and Text.EndsWith([Name], Suffix)
            ),

            // Sort to get newest file
            Sorted =
                if Table.HasColumns(Filtered, "Date modified")
                then Table.Sort(Filtered, {{"Date modified", Order.Descending}})
                else if Table.HasColumns(Filtered, "Date created")
                then Table.Sort(Filtered, {{"Date created", Order.Descending}})
                else Filtered,

            Latest =
                if Table.RowCount(Sorted) = 0 then null else Sorted{0},

            LatestPath =
                if Latest = null then null else Latest[Folder Path] & Latest[Name],

            LatestContent =
                if Latest = null then null else Latest[Content],

                //-----------------------------------------------------------
                // If no file → log error, otherwise call FileFunction
                //-----------------------------------------------------------
                FileResult =
                    if LatestPath = null then
                        [
                            Data = null,
                            Diagnostics = 
                            [
                                FilePath = "(none)",
                                Error = "No matching file",
                                RequestedColumns = WantedColumns,
                                MatchedColumns = {},
                                MissingColumns = WantedColumns
                            ]
                        ]
                    else
                        FileFunction(LatestContent, LatestPath, Sheet, WantedColumns),

                TableData   = FileResult[Data],
                Diagnostics = FileResult[Diagnostics],

                //-----------------------------------------------------------
                // Add Area + Model fields
                //-----------------------------------------------------------
                WithMeta =
                    if TableData = null then null else
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
            if Table.RowCount(Valid) = 0 then #table({}, {})
            else Table.Combine(Valid[Data]),

        //-----------------------------------------------------------
        // FULL CLEANING PIPELINE
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
            List.Transform(Table.ColumnNames(AsText), each {_, each if _ = null then "" else _, type text})
        ),

        // 4: Convert quantity safely
        QtyInt = Table.TransformColumns(
            NoNulls,
            {{"Quantity per Vehicle",
                each if _ = "" then null else Number.FromText(_),
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
                Text.From([First Five], ""),
                Text.From([Last Five], ""),
                Text.From([Last Two], "")
            }),
            type text
        ),

        // 7: Filter invalid part numbers
        FinalFiltered = Table.SelectRows(
            With12,
            each not List.Contains({"", null, "1", "*", " "}, [#"First Five"])
        )

    in
        [
            Data = FinalFiltered,
            Log = Log
        ]
in
    vuteq_configtable
```

New vuteq_mpm_file_data
```m
let
    get_configtable_data = (ConfigTable as table, FileFunction as function) =>
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
                SiteUrl    = [SiteUrl],
                FolderPath = [FolderPath],
                Pattern    = [FilePattern],
                Sheet      = [SheetName],

                // Column lists
                StandardCols = SplitSemi([StandardColumns]),

                DateCol =
                    if [DateColumn] = null or Text.Trim([DateColumn]) = ""
                    then null
                    else Text.Trim([DateColumn]),

                WantedColumns =
                    if DateCol = null
                    then StandardCols
                    else List.Combine({StandardCols, {DateCol}}),

                //-----------------------------------------------------------
                // Locate newest matching file from SharePoint
                //-----------------------------------------------------------
                AllFiles = SharePoint.Files(SiteUrl, [ApiVersion = 15]),

                InFolder = Table.SelectRows(AllFiles, each
                    Text.Contains([Folder Path], FolderPath)
                ),

                Prefix = Text.Trim(Text.BeforeDelimiter(Pattern, "*")),
                Suffix = Text.Trim(Text.AfterDelimiter(Pattern, "*")),

                Filtered = Table.SelectRows(InFolder, each
                    Text.StartsWith([Name], Prefix)
                    and Text.EndsWith([Name], Suffix)
                ),

                Sorted =
                    if Table.HasColumns(Filtered, "Date modified")
                    then Table.Sort(Filtered, {{"Date modified", Order.Descending}})
                    else if Table.HasColumns(Filtered, "Date created")
                    then Table.Sort(Filtered, {{"Date created", Order.Descending}})
                    else Filtered,

                Latest =
                    if Table.RowCount(Sorted) = 0 then null else Sorted{0},

                LatestPath =
                    if Latest = null then null else Latest[Folder Path] & Latest[Name],

                LatestContent =
                    if Latest = null then null else Latest[Content],

                //-----------------------------------------------------------
                // If no file -> log error. If file found, try FileFunction
                // and log a graceful error instead of crashing the whole query.
                //-----------------------------------------------------------
                FileResult =
                    if LatestPath = null then
                        [
                            Data = null,
                            Diagnostics =
                            [
                                FilePath = "(none)",
                                Error = "No matching file",
                                RequestedColumns = WantedColumns,
                                MatchedColumns = {},
                                MissingColumns = WantedColumns
                            ]
                        ]
                    else
                        let
                            AttemptResult = try FileFunction(LatestContent, LatestPath, Sheet, WantedColumns)
                        in
                            if AttemptResult[HasError] then
                                [
                                    Data = null,
                                    Diagnostics =
                                    [
                                        FilePath = LatestPath,
                                        Error = "FileFunction failed: " & AttemptResult[Error][Message],
                                        RequestedColumns = WantedColumns,
                                        MatchedColumns = {},
                                        MissingColumns = WantedColumns
                                    ]
                                ]
                            else
                                AttemptResult[Value],

                TableData   = FileResult[Data],
                Diagnostics = FileResult[Diagnostics],

                //-----------------------------------------------------------
                // Type StandardCols as Int64, DateCol as date
                //-----------------------------------------------------------
                ExistingStandardCols =
                    if TableData = null then {}
                    else List.Intersect({Table.ColumnNames(TableData), StandardCols}),

                ExistingDateCol =
                    if TableData = null or DateCol = null then {}
                    else List.Intersect({Table.ColumnNames(TableData), {DateCol}}),

                Typed =
                    if TableData = null then null
                    else
                        let
                            IntTyped = Table.TransformColumnTypes(
                                TableData,
                                List.Transform(ExistingStandardCols, each {_, Int64.Type})
                            ),
                            DateTyped = Table.TransformColumnTypes(
                                IntTyped,
                                List.Transform(ExistingDateCol, each {_, type date})
                            )
                        in
                            DateTyped
            in
                [
                    Data = Typed,
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
            if Table.RowCount(Valid) = 0 then #table({}, {})
            else Table.Combine(Valid[Data])

    in
        [
            Data = Combined,
            Log = Log
        ]
in
    get_configtable_data
```
