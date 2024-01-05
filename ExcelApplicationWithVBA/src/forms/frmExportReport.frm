VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmExportReport 
   Caption         =   "Exporta��es de Relat�rios"
   ClientHeight    =   3990
   ClientLeft      =   120
   ClientTop       =   460
   ClientWidth     =   5080
   OleObjectBlob   =   "frmExportReport.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmExportReport"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
#Const dMode = False

Private Sub CarregaComboAno(Source As String)
#If dMode Then
    Dim oDic As Scripting.Dictionary: Set oDic = New Scripting.Dictionary
#Else
    Dim oDic As Object: Set oDic = VBA.CreateObject("Scripting.Dictionary")
#End If
    Dim loConsultas     As ListObject
    Dim loProcedimentos As ListObject
    Dim lo              As ListObject
    Dim counter         As Long
    Dim item            As String
    
    Set loConsultas = wsConsultas.ListObjects("tbConsultas")
    Set loProcedimentos = wsProcedimentos.ListObjects("tbProcedimentos")
    Set lo = VBA.IIf(Source = "Consultas", loConsultas, loProcedimentos)
    
    For counter = 1 To lo.ListRows.Count
        item = lo.DataBodyRange(counter, lo.ListColumns("ANO").Index).Value2
        If Not oDic.Exists(item) Then oDic.Add item, item
    Next counter
    
    Me.ComboAno.List = oDic.Items
End Sub

Private Sub CarregaComboM�s(Consultas As Boolean)
#If dMode Then
    Dim oDic As Scripting.Dictionary: Set oDic = New Scripting.Dictionary
#Else
    Dim oDic As Object: Set oDic = VBA.CreateObject("Scripting.Dictionary")
#End If
    Dim loConsultas     As ListObject
    Dim loProcedimentos As ListObject
    Dim lo              As ListObject
    Dim counter         As Long
    Dim itemAno         As String
    Dim itemM�s         As String
    
    Set loConsultas = wsConsultas.ListObjects("tbConsultas")
    Set loProcedimentos = wsProcedimentos.ListObjects("tbProcedimentos")
    Set lo = VBA.IIf(Consultas, loConsultas, loProcedimentos)
    
    For counter = 1 To lo.ListRows.Count
        itemAno = lo.DataBodyRange(counter, lo.ListColumns("ANO").Index).Value2
        itemM�s = lo.DataBodyRange(counter, lo.ListColumns("M�S").Index).Value2
        
        If Not oDic.Exists(itemM�s) And itemAno = Me.ComboAno.Value Then
            oDic.Add itemM�s, itemM�s
        End If
        
    Next counter
    
    Me.ComboM�s.List = oDic.Items
End Sub

Private Sub btnExport_Click()
    If Not ValidateEmptyControls(Me) Then
        If Me.obtnConsultas.Value And Me.chkPDF.Value Then
            Call ExportReport(Consultas, Me.ComboAno.Value, Me.ComboM�s.Value, xlYes)
        ElseIf Me.obtnConsultas.Value And Not Me.chkPDF.Value Then
            Call ExportReport(Consultas, Me.ComboAno.Value, Me.ComboM�s.Value, xlNo)
        ElseIf Me.obtnProcedimentos.Value And Me.chkPDF.Value Then
            Call ExportReport(Procedimentos, Me.ComboAno.Value, Me.ComboM�s.Value, xlYes)
        Else
            Call ExportReport(Procedimentos, Me.ComboAno.Value, Me.ComboM�s.Value, xlNo)
        End If
    End If
    If Not MsgBox("Deseja realizar mais alguma opera��o?", vbQuestion + vbYesNo) = vbYes Then
        Unload Me
    End If
End Sub

Private Sub chkPDF_Click()
    With Me.chkPDF
        .Caption = VBA.IIf(.Value, "Gerar PDF!", "Gerar PDF?")
    End With
End Sub

Private Sub ComboAno_Exit(ByVal Cancel As MSForms.ReturnBoolean)
    Call CarregaComboM�s(Me.obtnConsultas)
End Sub

Private Sub fmReports_Enter()
    Me.ComboAno.Value = ""
    Me.ComboM�s.Value = ""
End Sub

Private Sub fmReports_Exit(ByVal Cancel As MSForms.ReturnBoolean)
    If Not Me.obtnConsultas.Value And Not Me.obtnProcedimentos.Value Then
        Cancel = True
    Else
        If Me.obtnConsultas Then Call CarregaComboAno("Consultas") Else Call CarregaComboAno("Procedimentos")
    End If
End Sub

Private Sub UserForm_Initialize()
    wsView.Activate
End Sub

