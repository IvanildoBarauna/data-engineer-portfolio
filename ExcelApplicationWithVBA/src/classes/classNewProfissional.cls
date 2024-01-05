VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "cNewProfissional"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit
Private Type ClassType
    sProfissional As String
    iCBO          As String
End Type

Private This As ClassType

Public Property Let NomeProfissional(Value As String): This.sProfissional = VBA.Strings.UCase(Value): End Property
Public Property Let cboProfissional(Value As String): This.iCBO = Value: End Property

Public Sub SaveOrChangeData(Optional RowIndex As Long = 0)
    Dim ws      As Excel.Worksheet
    Dim lo      As Excel.ListObject
    Dim lr      As Excel.ListRow
    
    Set ws = wsCadastros
    Set lo = ws.ListObjects("tbCadastroProfissional")
    
    If RowIndex > 0 Then
        Set lr = lo.ListRows(RowIndex)
    Else
        Set lr = lo.ListRows.Add
    End If
    
    With lr
        .Range(lo.ListColumns("PROFISSIONAL").Index).Value2 = This.sProfissional
        .Range(lo.ListColumns("Nº: CBO").Index).Value2 = This.iCBO
    End With
    
    Call SortListObject(lo, lo.ListColumns("PROFISSIONAL").Index, xlAscending, xlYes)
    ThisWorkbook.Save
End Sub
