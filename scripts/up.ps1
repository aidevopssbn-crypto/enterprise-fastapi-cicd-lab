Write-Host "Starting enterprise CI/CD lab..."
docker compose up -d --build
Write-Host "Jenkins:   http://localhost:8080"
Write-Host "SonarQube: http://localhost:9000"
