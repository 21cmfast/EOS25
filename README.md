# EOS25
All scipts required to reproduce the EOS25 simulation

<table><thead>
  <tr>
    <th>EOS25 simulation step<br></th>
    <th colspan="2">Computation time [hrs]</th>
    <th colspan="2">Memory [Tb]</th>
    <th colspan="2">Storage [Tb]</th>
    <th colspan="2">SUs</th>
  </tr></thead>
<tbody>
  <tr>
    <td></td>
    <td>Estimated</td>
    <td>Actual</td>
    <td>Estimated</td>
    <td>Actual</td>
    <td>Estimated</td>
    <td>Actual</td>
    <td>Estimated</td>
    <td>Actual</td>
  </tr>
  <tr>
    <td>Initial conditions</td>
    <td>11<br><br></td>
    <td>13.5 + 2.75 <br>for writing to disk</td>
    <td>2.5</td>
    <td>1.96</td>
    <td>1.2</td>
    <td>1.2</td>
    <td>800 EM</td>
    <td>1170.92</td>
  </tr>
  <tr>
    <td>One perturbed field<br></td>
    <td>0.75<br></td>
    <td>1.0</td>
    <td>0.43<br></td>
    <td>0.41</td>
    <td>43Gb x 92 = 4Tb</td>
    <td></td>
    <td>9k RM-512</td>
    <td>3k RM-512 + 22 EM</td>
  </tr>
  <tr>
    <td>Perturbed halo fields</td>
    <td>15</td>
    <td></td>
    <td>1.3</td>
    <td></td>
    <td>1</td>
    <td></td>
    <td>720 EM</td>
    <td></td>
  </tr>
  <tr>
    <td>Evolving astrophysics for one coeval</td>
    <td>7</td>
    <td></td>
    <td>3.5</td>
    <td></td>
    <td>2.6Tb x 92 = 240 Tb<br>0.215 x 92 = 20Tb without XRS<br></td>
    <td></td>
    <td>672 EM x 92 = 62k</td>
    <td></td>
  </tr>
</tbody></table>
