```ts
function main(workbook: ExcelScript.Workbook) {

  function stopStartScreenCalc(state: boolean) {
    workbook.enableCalculation(state);
  }

  stopStartScreenCalc(true);

  //const sheet = workbook.getWorksheet("Ergo Depot");
  const sheet = workbook.worksheets.getActiveWorksheet();

  if (!sheet) {
    throw new Error("Worksheet not found.");
  }

  const pivotTable = sheet.getPivotTable("PivotTable1");

  if (!pivotTable) {
    throw new Error("PivotTable 'PivotTable1' not found.");
  }

  const allHierarchies = pivotTable.getHierarchies();

  function getHierarchy(name: string): ExcelScript.PivotHierarchy {
    const h = allHierarchies.find(x => x.getName() === name);
    if (!h) {
      throw new Error(`Hierarchy not found: ${name}`);
    }
    return h;
  }

  function hasPivotHierarchy(
    collection: ExcelScript.PivotHierarchy[],
    name: string
  ): boolean {
    return collection.some(h => h.getName() === name);
  }

  function hasDataHierarchy(
    collection: ExcelScript.DataPivotHierarchy[],
    name: string
  ): boolean {
    return collection.some(h => h.getName() === name);
  }

  function safeRemoveRowHierarchy(name: string) {
    const hierarchy = pivotTable.getRowHierarchies().find(h => h.getName() === name);
    if (hierarchy) {
      pivotTable.removeRowHierarchy(hierarchy);
    }
  }

  function safeRemoveColumnHierarchy(name: string) {
    const hierarchy = pivotTable.getColumnHierarchies().find(h => h.getName() === name);
    if (hierarchy) {
      pivotTable.removeColumnHierarchy(hierarchy);
    }
  }

  function safeRemoveDataHierarchy(name: string) {
    const hierarchy = pivotTable.getDataHierarchies().find(h => h.getName() === name);
    if (hierarchy) {
      pivotTable.removeDataHierarchy(hierarchy);
    }
  }

  // Clear only the fields we care about
  safeRemoveRowHierarchy("ProjectStage");
  safeRemoveRowHierarchy("ProjectCode");
  safeRemoveRowHierarchy("MeasuredOn");

  safeRemoveColumnHierarchy("ProjectStage");
  safeRemoveColumnHierarchy("ProjectCode");
  safeRemoveColumnHierarchy("MeasuredOn");

  safeRemoveDataHierarchy("Actual  - Running Total by DateinActivity");
  safeRemoveDataHierarchy("Target Forces - Running Total by Measurement");

  // Rebuild rows
  if (!hasPivotHierarchy(pivotTable.getRowHierarchies(), "ProjectStage")) {
    pivotTable.addRowHierarchy(getHierarchy("ProjectStage"));
  }

  if (!hasPivotHierarchy(pivotTable.getRowHierarchies(), "ProjectCode")) {
    pivotTable.addRowHierarchy(getHierarchy("ProjectCode"));
  }

  if (!hasPivotHierarchy(pivotTable.getRowHierarchies(), "MeasuredOn")) {
    pivotTable.addRowHierarchy(getHierarchy("MeasuredOn"));
  }

  // Keep values in columns implicitly by adding data hierarchies
  if (!hasDataHierarchy(pivotTable.getDataHierarchies(), "Actual  - Running Total by DateinActivity")) {
    pivotTable.addDataHierarchy(getHierarchy("Actual  - Running Total by DateinActivity"));
  }

  if (!hasDataHierarchy(pivotTable.getDataHierarchies(), "Target Forces - Running Total by Measurement")) {
    pivotTable.addDataHierarchy(getHierarchy("Target Forces - Running Total by Measurement"));
  }

  const pivotLayout = pivotTable.layout;
  pivotLayout.layoutType = "Tabular";
  pivotLayout.layout.repeatAllItemLabels(true);

  sheet.getRange("F1").setValue("Pivot rebuilt with tabular layout and repeated labels");

  stopStartScreenCalc(false);
}
```
