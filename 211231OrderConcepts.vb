'Some VBA code made to order a long accounting sheet
'.vb used for formatting purposes

Sub order_concepts()
'starts at a3
Range("a3").Select

Dim separator As String
separator = " // "

Do While ActiveCell.Offset(0, 0).Range("b1").Value <> ""
    Do While ActiveCell.Value <> "" And ActiveCell.Offset(0, 0).Range("a2").Value = ""
        'DO NOT change offsets focus here
        'cuts whats below and unites that with whats above, with the separator
        ActiveCell.Offset(0, 0).Range("b1").Value = ActiveCell.Offset(0, 0).Range("b1").Value & separator & ActiveCell.Offset(0, 0).Range("b2").Value
        'deletes the row below
        ActiveCell.Offset(0, 0).Range("a2").EntireRow.Delete
        'activates once again the first active cell so that the loop repeats if necessary
    Loop
ActiveCell.Offset(1, 0).Range("a1").Select 'goes one row below, repeats

Loop
End Sub
