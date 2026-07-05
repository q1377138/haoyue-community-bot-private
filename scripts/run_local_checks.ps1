$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
python -m unittest discover -s tests
python -m bot.cli weekly-preview --balance 12 --community-bound true
python -m bot.cli service-group-button
python -m bot.cli daily-summary-schedule
python -m bot.cli knowledge-search 502 --dir tests\fixtures\knowledge
python -m bot.cli mention-reply "@q13771388"
python -m bot.cli mention-reply "@q13771388 帮我看下403是怎么回事"
