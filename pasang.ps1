# Pasang skill-edit-rizky + sutradara-edit ke %USERPROFILE%\.claude\skills (dengan cadangan)
$ErrorActionPreference = 'Stop'
$akar = Split-Path -Parent $MyInvocation.MyCommand.Path
$skills = Join-Path $env:USERPROFILE '.claude\skills'
$cadangan = Join-Path $env:USERPROFILE ('.claude\skills-cadangan\' + (Get-Date -Format 'yyyy-MM-dd HHmmss'))

New-Item -ItemType Directory -Force $skills | Out-Null
foreach ($nama in @('skill-edit-rizky', 'sutradara-edit', 'kolase-retro')) {
    $lama = Join-Path $skills $nama
    if (Test-Path $lama) {
        New-Item -ItemType Directory -Force $cadangan | Out-Null
        Move-Item $lama (Join-Path $cadangan $nama)
        Write-Output "cadangan: $nama -> $cadangan"
    }
}
foreach ($nama in @('skill-edit-rizky', 'sutradara-edit')) {
    $tujuan = Join-Path $skills $nama
    Copy-Item -Recurse (Join-Path $akar $nama) $tujuan
    if ($nama -eq 'skill-edit-rizky') { Copy-Item -Recurse (Join-Path $akar 'aset') (Join-Path $tujuan 'aset') }
    Get-ChildItem -Recurse $tujuan -Include '__pycache__' -Directory | Remove-Item -Recurse -Force
    Write-Output "terpasang: $tujuan"
}
