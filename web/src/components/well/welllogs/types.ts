


export type TableWellLogsInfo = (
  Pick<App.Well.WellLog, "name" | "unit" | "description"> & {
    _id?: App.Well.WellLog["_id"];
  }
)[];