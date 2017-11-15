$PROJECT = 'doct'
$ACTIVITIES = ['version_bump', 'changelog', 'tag', 'conda_forge']

$VERSION_BUMP_PATTERNS = [
    ('setup.py', '    version=\s*=.*', "        version='$VERSION'")
    ]
$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_IGNORE = ['TEMPLATE.rst']
$TAG_REMOTE = 'git@github.com:NSLS-II/doct.git'

$GITHUB_ORG = 'NSLS-II'
$GITHUB_REPO = 'doct'
