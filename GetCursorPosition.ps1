Function Pause ($Message = "Press a key to get cursor position: ") 
{
   # Check if running in PowerShell ISE
   If ($psISE) {
      # "ReadKey" not supported in PowerShell ISE.
      # Show MessageBox UI
      $Shell = New-Object -ComObject "WScript.Shell"
      $Button = $Shell.Popup("Click OK to continue.", 0, "Hello", 0)
      Return
   }
 
   Write-Host -NoNewline $Message
   While ($KeyInfo.VirtualKeyCode -Eq $Null -Or $Ignore -Contains $KeyInfo.VirtualKeyCode) {
      $KeyInfo = $Host.UI.RawUI.ReadKey("NoEcho, IncludeKeyDown")
   }
}

while($true)
{
    pause
      
    Add-Type -AssemblyName System.Windows.Forms
 
    $X = [System.Windows.Forms.Cursor]::Position.X
    $Y = [System.Windows.Forms.Cursor]::Position.Y
 
    Write-Output "X: $X | Y: $Y"
}

      

