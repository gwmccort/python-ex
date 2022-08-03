# %%
import pandas as pd
import rms_playlist as pl


# %%
new_df = pl.parse_html(pl.read_url(pl.BG_SONGS_URL))
old_df = pd.read_csv(pl.BG_SONG_CSV_FILE)
m_df = pl.merge_frames(old_df, new_df)

# %%
help(pl)

# %%
