$file = 'c:\Users\pelew\Documents\CYBER DEV POTOTFOLOIO\INDEX.HTML'
$content = Get-Content $file -Raw

$content = $content -replace '<p>📱 <strong>08075793311</strong></p>', ''
$content = $content -replace '<p>📱 08075793311</p>', ''
$content = $content -replace '2348075793311', ''
$content = $content -replace '.*whatsapp-btn.*\n', ''

Set-Content $file $content
Write-Host 'Done'
