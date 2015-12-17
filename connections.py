# list of connections between Vampires
# for IDs, see vampy.py (or vampires_dus.db)
# (8): connected-from ID, connected-to ID, bi-directional, connection type, connection details, start date, end date, misc
connections = [
    (1, 2, 1, "coterie", None, None, None, None),# Hauke and Valeria
    (1, 3, 1, "coterie", None, None, None, None),# Hauke and Sven
    (1, 4, 1, "coterie", None, None, None, None),# Hauke and Fred
    (2, 3, 1, "coterie", None, None, None, None),# Valeria and Sven
    (2, 4, 1, "coterie", None, None, None, None),# Valeria and Fred
    (3, 4, 1, "coterie", None, None, None, None),# Fred and Sven
    # Parens
    (3, 14, 0, "childer", None, None, None, None),# Sven and Baron
    # Mentor
    (3, 15, 0, "protege", None, None, None, None),# Sven and Welsh
    (1, 12, 0, "protege", None, None, None, None),# Hauke and Rosenberg
    (10, 17, 0, "protege", "former", None, None, None),# Lucretia and Uhrmacher
    (29, 27, 0, "protege", None, None, None, None),# Asmodius and Architekt
    # politics
    (10, 41, 0, "political allegiance", None, None, None, None),# Lucretia to Kürten
    (15, 14, 0, "political allegiance", None, None, None, None),# Welsh to Baron
    (12, 11, 0, "political allegiance", None, None, None, None),# Rosenberg to Prince
    (13, 11, 0, "political allegiance", None, None, None, None),# Sebastian to Prince
    (16, 14, 0, "political allegiance", None, None, None, None),# Mara to Baron
    (17, 14, 0, "political allegiance", None, None, None, None),# Uhrmacher to Baron
    (18, 14, 0, "political allegiance", None, None, None, None),# Henri to Baron
    (21, 19, 0, "political allegiance", None, None, None, None),# Mutter Ey to Elise (Synode)
    (22, 19, 0, "political allegiance", None, None, None, None),# Wolfi to Elise
    (23, 19, 0, "political allegiance", None, None, None, None),# Biene to Elise
    (25, 14, 0, "political allegiance", None, None, None, None),# Ratte to Baron
    #(24, )# Alois is his own prince
    (26, 11, 0, "political allegiance", None, None, None, None),# Matsumoto to Prince
    (27, 11, 0, "political allegiance", None, None, None, None),# Architekt to Prince
    (27, 41, 0, "political allegiance", None, None, None, None),# Architekt to Kürten
    #(28, ) Philosoph is nothing and everything (Kogaion)
    (29, 11, 0, "political allegiance", None, None, None, None),# Asmodius to Prince
    (30, 31, 0, "political allegiance", None, None, None, None),# Sommerfeld to Braunberg
    (31, 24, 0, "political allegiance", None, None, None, None),# Braunberg to Alois
    #(32, )# Noach
    (33, 24, 0, "political allegiance", None, None, None, None),# Dr. Austein to Alois
    (34, 24, 0, "political allegiance", None, None, None, None),# Hamish to Alois
    (35, 41, 0, "political allegiance", None, None, None, None),# Ziller to Kürten
    #(36, )# Anja, Paladin of Lancea Sancta
    #(37, )# Maria to ?
    #(38, )# Adrian von Langenfelden
    #(39, )# Weitenau
    #(40, )# Brauner, Erzbischof of Lancea Sancta
    # friendship
    (14, 15, 1, "friendship", None, None, None, None),# Welsh to Baron
    (19, 11, 1, "friendship", None, None, None, None),# Elise to Prince
    (22, 23, 1, "friendship", None, None, None, None)# Wolfi to Biene
    # enemies
    #(, , 0, "", None, None, None, None)
]
