# Moved from TLS-App Docs/TLETS/scripts/update-azure-inventories.ps1 on 2026-11-14.
# Refresh Azure inventory facts for TLETS agency tenants.
# Requires: Azure CLI logged into Azure Government (TLS Azure Subscription 1)
# Usage: ./update-azure-inventories.ps1
#        ./update-azure-inventories.ps1 -Tenant slatontx

param(
    [ValidateSet('slatontx', 'crosbytx', 'littlefieldtx', 'crystalcitypd', 'levellandtx', 'all')]
    [string] $Tenant = 'all'
)

$ErrorActionPreference = 'Stop'

$tenants = @{
    slatontx       = @{ Db = 'tls-slatontx-prod-rms';       Api = 'tls-slatontx-prod-api';       Ui = 'tls-slatontx-prod-ui' }
    crosbytx       = @{ Db = 'tls-crosbytx-prod-rms';       Api = 'tls-crosbytx-prod-api';       Ui = 'tls-crosbytx-prod-ui' }
    littlefieldtx  = @{ Db = 'tls-littlefieldtx-prod-rms';  Api = 'tls-littlefieldtx-prod-api';  Ui = 'tls-littlefieldtx-prod-ui' }
    crystalcitypd  = @{ Db = 'tls-crystalcitypd-prod-rms';  Api = 'tls-crystalcitypd-prod-api';  Ui = 'tls-crystalcitypd-prod-ui' }
    levellandtx    = @{ Db = 'tls-levellandtx-prod-rms';    Api = 'tls-levellandtx-prod-api';    Ui = 'tls-levellandtx-prod-ui' }
}

$selected = if ($Tenant -eq 'all') { $tenants.Keys } else { @($Tenant) }

Write-Host "Azure cloud:" (az cloud show --query name -o tsv)
Write-Host "Subscription:" (az account show --query name -o tsv)
Write-Host ""

foreach ($key in $selected) {
    $t = $tenants[$key]
    Write-Host "=== $key ==="
    Write-Host "TDE:" (az sql db tde show -g tls --server tls-db2 --name $t.Db --query state -o tsv)
    $ltr = az sql db ltr-policy show -g tls --server tls-db2 --name $t.Db -o json | ConvertFrom-Json
    Write-Host "LTR: weekly=$($ltr.weeklyRetention) monthly=$($ltr.monthlyRetention) yearly=$($ltr.yearlyRetention) immutability=$($ltr.timeBasedImmutability)"
    az webapp show -g tls -n $t.Api --query "{name:name,host:defaultHostName,location:location}" -o json
    az webapp show -g tls -n $t.Ui --query "{name:name,host:defaultHostName,location:location}" -o json
    Write-Host ""
}

Write-Host "Update the matching agencies/*/azure-inventory.md Last refreshed date and tables manually from this output."
