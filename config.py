import dash_html_components as html


# parameters for the Elo algorithm -- setting kind of arbitrarily for now, should tune once we have more data
DEFAULT_K_VALUE = 32
DEFAULT_D_VALUE = 400
DEFAULT_SCORING_FUNCTION_BASE = 2.0
INITIAL_RATING = 1000

# Google Sheets info for reading input data
GSHEETS_CREDENTIALS_FILE = "./google-credentials.json"
SPREADSHEET_ID = "1FfodGHcgy8Xh1IucHC3-JgcDd7o7PLVojUMrNodNg0I"
DATA_SHEET_ID = 295324701
DUMMY_PLAYER_NAME = "_dummy_"

# dashboard settings
DBC_THEME = "FLATLY"  # others I liked: DARKLY, SIMPLEX, LUMEN (https://bootswatch.com/flatly/)
PLOTLY_THEME = "plotly_white"
LOGO_PATH = "/assets/vp.jpeg"
GITHUB_LOGO_PATH = "assets/GitHub-Mark-32px.png"
GITHUB_URL = "https://github.com/DanielPBak/dune-elo-dashboard"
TITLE = "Dune: Imperium - Ranked"
SUBTITLE = ["Submit form responses ", html.A("here", href="https://forms.gle/mhb5zzNmV7QzJicP6")]
