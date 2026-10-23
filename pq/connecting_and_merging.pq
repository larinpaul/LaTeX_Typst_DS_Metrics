// Connecting to a SQL Database and Merging Columns

let
    // Connect to the local SQL server database
    SqlSource = Sql.Database("sql-srv-01.company.local", "Erp_db"),

    // Select the specific "Customers" table from the database schema
    CustomersTable = SqlSource{[Schema="dbo", Item="Customers"]}[Data],

    // Combine First Name and Last Name into a single "Full Name" column
    MergedColumns = Table.CombineColumns(CustomersTable, {"FirstName", "LastName"}, Combiner.CombineTextByDelimiter(" ", QuoteStyle.None), "Full Name"),

    // Renmove an unnecessary technical ID column to clean up the output
    RemovColumns = Table.RemoveColumns(MergedColumns, {"TechnicalID"})
in
    RemovedColumns
