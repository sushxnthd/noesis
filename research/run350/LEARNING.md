# LEARNING ledger — Run 350
New cohort seeds 33000..33191; 192 width-three ReLU recurrent models; 200 Adam updates; original Run348 parity training with only seed range changed.
Ten endpoints satisfy independently checked unrestricted-correctness certificates. Two networks demonstrate exact representational changes while training accuracy remains 100%:
- 33053: epoch 30 to 31, BCE 0.48587741824811376 to 0.4602176511893052; exact affine obstruction at 30, exact separator on 2,644 fixed words at 31; unrestricted certified at 76.
- 33068: epoch 55 to 56, BCE 0.1599659767857383 to 0.1525503326218604; exact affine obstruction at 55, exact separator on 2,644 fixed words at 56; unrestricted certified at 72.
Original early output heads fail on witness words despite exact 510/510 short-input correctness. No assertion that the exact algorithm acquisition event occurs at the one-step finite-family repairability transition.
Protocol-defined success count: 2 seeds, criterion >=1, PASS. This is not a universal acquisition law.
