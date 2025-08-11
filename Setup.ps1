# MJ-NEXARA Setup.ps1 — Intelligent Fallback Version

# 🌐 Show current path
Write-Host "📍 Current Directory: $PWD" -ForegroundColor Cyan

# 🧠 Check if running from MJ-NEXARA folder
if ($PWD.Path -notlike "*MJ-NEXARA*") {
    Write-Host "⚠️ Warning: You are not inside the MJ-NEXARA folder!" -ForegroundColor Yellow
    Write-Host "💡 Tip: Move this script to C:\Projects\MJ-NEXARA or run it from there." -ForegroundColor Yellow
    exit
}

# 📁 Ensure essential folders exist
$folders = @("mj-docs", "nexara-utils", "nexara-protocol", "LumID", "NexMart", "NexaraGov")
foreach ($folder in $folders) {
    $path = "C:\Projects\$folder"
    if (-not (Test-Path $path)) {
        Write-Host "📁 Creating missing folder: $folder"
        New-Item -ItemType Directory -Path $path | Out-Null
    } else {
        Write-Host "✅ Found: $folder"
    }
}

# ⚙️ MJ Setup Complete
Write-Host "$([char]0x2705) MJ Setup Complete!" -ForegroundColor Green
Write-Host "🚀 Ready to launch MJ-NEXARA modules!" -ForegroundColor Magenta
