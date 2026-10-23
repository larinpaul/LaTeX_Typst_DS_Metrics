// It automates the process of opening a raw sales report, setting up headers, and filtering the data.

let
    // 1. Connect to the source data (a local CSV file)
    Source = Csv.Document(File.Contents("C:\Data\Sales2026.csv"), [Delimiter=";", Columns=4, Encoding=1251, QuoteStyle=QuoteStyle.None]),

    // 2. Promote the first row of data to be the column headers
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalarTypes=true]),

    // 3. Define data types for each column (Text, Integer, Date)
    ChangedType = Table.TransformColumnTypes(PromotedHeaders, {{"Region", type text}, {"Amount", Int64.Type}, {"Date", type date}}),

    // 4. Filter the rows to only keep European sales data
    FilteredRows = Table.SelectRows(ChangedType, each ([Region] = "Europe"))

in
    FilteredRows
