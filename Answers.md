```m
let
    parse_configtable = (ConfigTable as table, FileFunction as function) =>
    
    // Helper: delimiter splitter
    let
        SplitText = (txt as nullable text, delimiter as text) as list =>
            let
                cleaned = 
                    if txt = null then "" 
                    else Text.Trim(txt),
                split = 
                    if cleaned= "" then {} 
                    else List.Transform(Text.Split(cleaned, delimiter), Text.Trim),
                nonBlank = List.Select(split, each _ <> "")
            in
                nonBlank,



    // Helper: parse lists
    let
        ParseList = (column as text, delimiter as text) as list =>
            if column = null or column = "" then {}
            else if List.Count(column) > 1 then SplitText(column, delimiter)
            else column
    in
        ParseList,
        // Load each file defined in ConfigTable
        AddResults = Table.AddColumn(ConfigTable, "Results", each
            let
                FolderPath            = [FolderPath],
                Pattern               = [FileName],
                Sheet                 = [SheetName],
                EndingDelimiter       = Text.Lower([FileDelimiter]),
                FileExtension         = Text.Lower([FileExtension]),
                TextCols              = SplitText([TextColumns], [SplitDelimiter]),               
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
