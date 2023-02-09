$path = "C:\Users\yizongk\Desktop\CandCMaterials\WorldCupCasino\WebhookListener"


## DON'T CHANGE ANYTHING BELOW THIS LINE
$port = 8083

if ( -not ( Test-Path -Path $path ) ) {
    throw "Path doesn't exist: '$path'"
}
cd $path

if ( -not ( "env/" | Test-Path ) ) {
    echo "Python env/ doesn't exists, creating it now..."
    python -m venv env
}
env\Scripts\Activate.ps1
echo "Installing any missing python dependencies..."
python -m pip install -r python_dependencies.txt | out-null

uvicorn main:app --reload --host localhost --port $port