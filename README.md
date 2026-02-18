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
    <td>13.5 + 2.75 <br>for writing to disk<br><br></td>
    <td></td>
    <td>1.96</td>
    <td></td>
    <td>1.2</td>
    <td></td>
    <td>800 EM</td>
    <td></td>
  </tr>
  <tr>
    <td>One perturbed field<br></td>
    <td>0.6<br></td>
    <td></td>
    <td>0.25<br></td>
    <td></td>
    <td>43Gb x 92 = 4Tb</td>
    <td></td>
    <td>9k RM-shared</td>
    <td></td>
  </tr>
  <tr>
    <td>Perturbed halo fields</td>
    <td>10</td>
    <td></td>
    <td>0.71</td>
    <td></td>
    <td>1</td>
    <td></td>
    <td>720 EM</td>
    <td>847 EM</td>
  </tr>
  <tr>
    <td>Evolving astrophysics for one coeval</td>
    <td>7</td>
    <td></td>
    <td>3.65</td>
    <td></td>
    <td>2.6Tb x 92 = 240 Tb<br>0.215 x 92 = 20Tb without XRS<br></td>
    <td></td>
    <td>672 EM x 92 = 62k</td>
    <td></td>
  </tr>
</tbody></table>
