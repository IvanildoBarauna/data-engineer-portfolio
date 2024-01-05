Attribute VB_Name = "mdRibbonsControls"
Option Explicit
Option Private Module
Sub RibbonsCallBacks(xControl As IRibbonControl)
    Dim CallName As String
    
    CallName = "'" & ThisWorkbook.Name & "'!" & "mdRibbonsControls." & xControl.ID
    
    Application.Run CallName
End Sub

Private Sub btLancamentos(): frmConsultas.Show: End Sub

Private Sub btreportfichas()
    On Error GoTo err:
    wsReportConsultas.Activate
    wsReportConsultas.PivotTables(1).RefreshTable
    VBA.MsgBox "O relat�rio est� atualizado.", vbInformation
    Exit Sub
err:
    MsgBox "N�o foi poss�vel atualizar o relat�rio." & vbNewLine & _
            err.Number & "-" & err.Description, vbCritical
End Sub

Private Sub btRelatorio()
    On Error GoTo err:
    wsReportProcedimentos.Activate
    wsReportProcedimentos.PivotTables(1).RefreshTable
    VBA.MsgBox "O relat�rio est� atualizado.", vbInformation
    Exit Sub
err:
    MsgBox "N�o foi poss�vel atualizar o relat�rio." & vbNewLine & _
            err.Number & "-" & err.Description, vbCritical
End Sub

Private Sub btprint(): frmExportReport.Show False: End Sub
Private Sub btProcedimentos(): frmProcedimentos.Show: End Sub
Private Sub btProfissional(): frmCadastroProfissional.Show: End Sub
Private Sub btProcedimento(): frmCadastroProcedimento.Show: End Sub
Private Sub btConsulta(): frmCadastroConsulta.Show: End Sub
Private Sub btCadastroView(): wsCadastros.Activate: End Sub

