
def sorted_by(g, p):
  if g[0] == p[0]:
    return -1 if g[1].lower() < p[1].lower() else 1 if g[1].lower() > p[1].lower() else 0
  else:
    return g[0] - p[0]


