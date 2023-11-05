Spark session created.
Data loaded.
Query executed: SELECT Name FROM baseball_table WHERE Team = 'WAS' and PosCategory = 'Pitcher' LIMIT 10
|    | Name           |
|---:|:---------------|
|  0 | Billy_Traber   |
|  1 | Tim_Redding    |
|  2 | John_Patterson |
|  3 | Shawn_Hill     |
|  4 | Joel_Hanrahan  |
|  5 | Mike_O'Connor  |
|  6 | Emiliano_Fruto |
|  7 | Chris_Schroder |
|  8 | Brett_Campbell |
|  9 | Beltran_Perez  |
Data transformed: Grouped by team and position and counted the number of players
|     | Team   | PosCategory   |   count |
|----:|:-------|:--------------|--------:|
|   0 | ANA    | Catcher       |       3 |
|   1 | ANA    | Infielder     |       9 |
|   2 | ANA    | Outfielder    |       8 |
|   3 | ANA    | Pitcher       |      15 |
|   4 | ARZ    | Catcher       |       2 |
|   5 | ARZ    | Infielder     |       7 |
|   6 | ARZ    | Outfielder    |       5 |
|   7 | ARZ    | Pitcher       |      14 |
|   8 | ATL    | Catcher       |       2 |
|   9 | ATL    | Infielder     |       8 |
|  10 | ATL    | Outfielder    |       7 |
|  11 | ATL    | Pitcher       |      20 |
|  12 | BAL    | Catcher       |       3 |
|  13 | BAL    | Infielder     |       6 |
|  14 | BAL    | Outfielder    |       7 |
|  15 | BAL    | Pitcher       |      18 |
|  16 | BOS    | Catcher       |       3 |
|  17 | BOS    | Infielder     |       5 |
|  18 | BOS    | Outfielder    |       7 |
|  19 | BOS    | Pitcher       |      20 |
|  20 | CHC    | Catcher       |       3 |
|  21 | CHC    | Infielder     |       6 |
|  22 | CHC    | Outfielder    |       8 |
|  23 | CHC    | Pitcher       |      19 |
|  24 | CIN    | Catcher       |       3 |
|  25 | CIN    | Infielder     |       8 |
|  26 | CIN    | Outfielder    |       8 |
|  27 | CIN    | Pitcher       |      16 |
|  28 | CLE    | Catcher       |       2 |
|  29 | CLE    | Infielder     |       6 |
|  30 | CLE    | Outfielder    |       8 |
|  31 | CLE    | Pitcher       |      18 |
|  32 | COL    | Catcher       |       3 |
|  33 | COL    | Infielder     |       6 |
|  34 | COL    | Outfielder    |       7 |
|  35 | COL    | Pitcher       |      18 |
|  36 | CWS    | Catcher       |       2 |
|  37 | CWS    | Infielder     |       6 |
|  38 | CWS    | Outfielder    |       8 |
|  39 | CWS    | Pitcher       |      15 |
|  40 | DET    | Catcher       |       2 |
|  41 | DET    | Infielder     |       9 |
|  42 | DET    | Outfielder    |       6 |
|  43 | DET    | Pitcher       |      19 |
|  44 | FLA    | Catcher       |       2 |
|  45 | FLA    | Infielder     |       6 |
|  46 | FLA    | Outfielder    |       7 |
|  47 | FLA    | Pitcher       |      17 |
|  48 | HOU    | Catcher       |       3 |
|  49 | HOU    | Infielder     |       9 |
|  50 | HOU    | Outfielder    |       5 |
|  51 | HOU    | Pitcher       |      17 |
|  52 | KC     | Catcher       |       2 |
|  53 | KC     | Infielder     |       8 |
|  54 | KC     | Outfielder    |       6 |
|  55 | KC     | Pitcher       |      18 |
|  56 | LA     | Catcher       |       2 |
|  57 | LA     | Infielder     |       9 |
|  58 | LA     | Outfielder    |       6 |
|  59 | LA     | Pitcher       |      16 |
|  60 | MIN    | Catcher       |       3 |
|  61 | MIN    | Infielder     |       8 |
|  62 | MIN    | Outfielder    |       5 |
|  63 | MIN    | Pitcher       |      15 |
|  64 | MLW    | Catcher       |       4 |
|  65 | MLW    | Infielder     |       8 |
|  66 | MLW    | Outfielder    |       8 |
|  67 | MLW    | Pitcher       |      15 |
|  68 | NYM    | Catcher       |       2 |
|  69 | NYM    | Infielder     |       7 |
|  70 | NYM    | Outfielder    |       7 |
|  71 | NYM    | Pitcher       |      22 |
|  72 | NYY    | Catcher       |       2 |
|  73 | NYY    | Infielder     |       7 |
|  74 | NYY    | Outfielder    |       5 |
|  75 | NYY    | Pitcher       |      17 |
|  76 | OAK    | Catcher       |       3 |
|  77 | OAK    | Infielder     |       9 |
|  78 | OAK    | Outfielder    |       5 |
|  79 | OAK    | Pitcher       |      19 |
|  80 | PHI    | Catcher       |       4 |
|  81 | PHI    | Infielder     |       6 |
|  82 | PHI    | Outfielder    |       6 |
|  83 | PHI    | Pitcher       |      19 |
|  84 | PIT    | Catcher       |       2 |
|  85 | PIT    | Infielder     |       6 |
|  86 | PIT    | Outfielder    |       7 |
|  87 | PIT    | Pitcher       |      20 |
|  88 | SD     | Catcher       |       2 |
|  89 | SD     | Infielder     |       5 |
|  90 | SD     | Outfielder    |       7 |
|  91 | SD     | Pitcher       |      18 |
|  92 | SEA    | Catcher       |       2 |
|  93 | SEA    | Infielder     |       7 |
|  94 | SEA    | Outfielder    |       7 |
|  95 | SEA    | Pitcher       |      18 |
|  96 | SF     | Catcher       |       2 |
|  97 | SF     | Infielder     |       7 |
|  98 | SF     | Outfielder    |       7 |
|  99 | SF     | Pitcher       |      18 |
| 100 | STL    | Catcher       |       2 |
| 101 | STL    | Infielder     |       7 |
| 102 | STL    | Outfielder    |       6 |
| 103 | STL    | Pitcher       |      17 |
| 104 | TB     | Catcher       |       3 |
| 105 | TB     | Infielder     |       5 |
| 106 | TB     | Outfielder    |       5 |
| 107 | TB     | Pitcher       |      19 |
| 108 | TEX    | Catcher       |       4 |
| 109 | TEX    | Infielder     |       5 |
| 110 | TEX    | Outfielder    |       6 |
| 111 | TEX    | Pitcher       |      19 |
| 112 | TOR    | Catcher       |       2 |
| 113 | TOR    | Infielder     |       8 |
| 114 | TOR    | Outfielder    |       3 |
| 115 | TOR    | Pitcher       |      19 |
| 116 | WAS    | Catcher       |       2 |
| 117 | WAS    | Infielder     |       7 |
| 118 | WAS    | Outfielder    |       7 |
| 119 | WAS    | Pitcher       |      20 |
Spark session stopped.
