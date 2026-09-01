# Your Real External Source

Unlike prior modules, this project doesn't pick a data **domain** — you
already have one, from Module 3/8. What's new here is the **source**:
a real external API your pipeline extracts from, on its own schedule,
independent of your existing warehouse data. Pick one.

## Option 1: Open-Meteo (recommended default)

**No API key required.** Real, live, no-auth weather forecast data,
confirmed reachable this session:

```
GET https://api.open-meteo.com/v1/forecast
    ?latitude=<lat>&longitude=<lon>
    &hourly=temperature_2m,precipitation
    &timezone=America%2FNew_York
```

Returns real hourly forecast data (temperature, precipitation) for the
coordinates you give it. **License:** CC BY 4.0 — real attribution
required if you publish results (cite Open-Meteo). Good fit for a
`@daily` or `@hourly` schedule — the forecast genuinely updates.

## Option 2: NASA Open APIs

**Requires a free personal API key** (beyond the shared `DEMO_KEY`
rate limit — get one at `api.nasa.gov`, costs nothing). Real, live, U.S.
Government Work (public domain). Multiple real endpoints — e.g. the
Astronomy Picture of the Day API, or near-Earth object data — pick one
that gives you real, structured fields worth loading into a table (not
just an image URL).

## Either way

- Your DAG's `extract` task should raise a real exception on a real
  failure (a bad response, a timeout) — that's what makes your retry
  configuration meaningful. Don't swallow errors just to make the task
  "succeed."
- Your `load` task writes into a **new table** in your own Module 3/8
  warehouse — this is new data, not overwriting your existing domain
  tables.
