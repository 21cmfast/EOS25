# EOS25
All scipts required to reproduce the EOS25 simulation

<table class="tg"><thead>
  <tr>
    <th class="tg-roi2" rowspan="2">EOS25 simulation step<br></th>
    <th class="tg-llyw" colspan="2">Computation time [hrs]</th>
    <th class="tg-llyw" colspan="2">Memory [Tb]</th>
    <th class="tg-llyw" colspan="2">Storage [Tb]</th>
    <th class="tg-llyw" colspan="2">SUs</th>
  </tr>
  <tr>
    <th class="tg-d52n">Estimated</th>
    <th class="tg-tw5s">Actual</th>
    <th class="tg-d52n">Estimated</th>
    <th class="tg-tw5s">Actual</th>
    <th class="tg-d52n">Estimated</th>
    <th class="tg-tw5s">Actual</th>
    <th class="tg-d52n">Estimated</th>
    <th class="tg-tw5s">Actual</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-c6of">Initial conditions</td>
    <td class="tg-7od5">11<br><br></td>
    <td class="tg-90e1">13.5</td>
    <td class="tg-7od5">2.5</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">1.2</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">800 EM</td>
    <td class="tg-90e1"></td>
  </tr>
  <tr>
    <td class="tg-0pky">One perturbed field<br></td>
    <td class="tg-7od5">0.75<br></td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">0.43<br></td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">43Gb x 92 = 4Tb</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">9k RM-512</td>
    <td class="tg-90e1"></td>
  </tr>
  <tr>
    <td class="tg-c6of">Perturbed halo field</td>
    <td class="tg-7od5">15</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">1.3</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">1</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">720 EM</td>
    <td class="tg-90e1"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Evolving astrophysics for one coeval</td>
    <td class="tg-7od5">7</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">3.5</td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">2.6Tb x 92 = 240 Tb<br>0.215 x 92 = 20Tb without XRS<br></td>
    <td class="tg-90e1"></td>
    <td class="tg-7od5">672 EM x 92 = 62k</td>
    <td class="tg-90e1"></td>
  </tr>
</tbody></table>
