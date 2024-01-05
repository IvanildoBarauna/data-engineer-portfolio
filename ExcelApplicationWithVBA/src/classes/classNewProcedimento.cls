VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "cNewProcedimento"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit
Private Type ClassType
    sProcedimento As String
    iCodigo       As String
End Type

Private This As ClassType

Public Property Let NomeProcedimento(Value As String): This.sProcedimento = VBA.Strings.UCase(Value): End Property
Public Property Let CodigoProcedimento(Value As String): This.iCodigo = Value: End Property

Public Sub SaveOrChangeData(Optional RowIndex As Long = 0)
    Dim lo      As Excel.ListObject
    Dim lr      As Excel.ListRow
    
    Set lo = wsCadastros.ListObjects("tbCadastroProcedimento")
    
    If RowIndex > 0 Then
        Set lr = lo.ListRows(RowIndex)
    Else
        Set lr = lo.ListRows.Add
    End If
    
    With lr
        .Range(lo.ListColumns("PROCEDIMENTO").Index).Value2 = This.sProcedimento
        .Range(lo.ListColumns("CÓD. PROCED.").Index).Value2 = This.iCodigo
    End With
    
    Call SortListObject(lo, lo.ListColumns("PROCEDIMENTO").Index, xlAscending, xlYes)
    ThisWorkbook.Save
End Sub
