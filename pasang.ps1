# Pasang skill-edit-rizky ke %USERPROFILE%\.claude\skills (dengan cadangan)
$ErrorActionPreference = 'Stop'
$akar = Split-Path -Parent $MyInvocation.MyCommand.Path
$skills = Join-Path $env:USERPROFILE '.claude\skills'
$tujuan = Join-Path $skills 'skill-edit-rizky'
$cadangan = Join-Path $env:USERPROFILE ('.claude\skills-cadangan\' + (Get-Date -Format 'yyyy-MM-dd HHmmss'))

New-Item -ItemType Directory -Force $skills | Out-Null
foreach ($lama in @($tujuan, (Join-Path $skills 'kolase-retro'))) {
    if (Test-Path $lama) {
        New-Item -ItemType Directory -Force $cadangan | Out-Null
        Move-Item $lama (Join-Path $cadangan (Split-Path -Leaf $lama))
        Write-Output "cadangan: $(Split-Path -Leaf $lama) -> $cadangan"
    }
}
Copy-Item -Recurse (Join-Path $akar 'skill-edit-rizky') $tujuan
Copy-Item -Recurse (Join-Path $akar 'aset') (Join-Path $tujuan 'aset')
Get-ChildItem -Recurse $tujuan -Include '__pycache__' -Directory | Remove-Item -Recurse -Force
Write-Output "terpasang: $tujuan"
