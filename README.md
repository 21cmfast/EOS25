# EOS25
All scipts required to reproduce the EOS25 simulation
|         EOS25 simulation step        | Computation time [hrs] |        | Memory [Tb] | Description | Storage [Tb]                                      |        | SUs               |        |
|:------------------------------------:|------------------------|--------|-------------|-------------|---------------------------------------------------|--------|-------------------|--------|
|                                      | Estimated              | Actual | Estimated   | Actual      | Estimated                                         | Actual | Estimated         | Actual |
| Initial conditions                   | 11                     | 13.5   | 2.5         |             | 1.2                                               |        | 800 EM            |        |
| One perturbed field                  | 0.75                   |        | 0.43        |             | 43Gb x 92 = 4Tb                                   |        | 9k RM-512         |        |
| Perturbed halo field                 | 15                     |        | 1.3         |             | 1                                                 |        | 720 EM            |        |
| Evolving astrophysics for one coeval | 7                      |        | 3.5         |             | 2.6Tb x 92 = 240 Tb 0.215 x 92 = 20Tb without XRS |        | 672 EM x 92 = 62k |        |
