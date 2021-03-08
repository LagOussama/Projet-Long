import {Component, Input, OnInit} from '@angular/core';
import * as CanvasJS from '../../assets/canvasjs.min';

@Component({
  selector: 'app-protocole-plot',
  templateUrl: './protocole-plot.component.html',
  styleUrls: ['./protocole-plot.component.css']
})
export class ProtocolePlotComponent implements OnInit {

  constructor() { }

  @Input() Message2 : any

  ngOnInit(): void {

    let dataPoints = [];

    console.log(this.Message2.result.length);

    for(let tmpNetwork of this.Message2.result){
      dataPoints.push({ label: tmpNetwork._id, y: Number(tmpNetwork.nb_packet)});
    }
    let y = 0;

    let chart = new CanvasJS.Chart("chartContainer", {
      animationEnabled: true,
      exportEnabled: true,
      title: {
        text: "Protocol Use Per packet"
      },
      data: [{
        type: "column",
        dataPoints: dataPoints
      }]
    });

    chart.render();
  }

}
