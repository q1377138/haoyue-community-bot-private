$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
python -m unittest discover -s tests
python -m bot.cli weekly-preview --balance 12 --community-bound true
python -m bot.cli service-group-button

