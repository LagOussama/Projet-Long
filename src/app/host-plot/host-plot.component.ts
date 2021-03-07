import { Component, OnInit } from '@angular/core';
import * as CanvasJS from '../../assets/canvasjs.min';


@Component({
  selector: 'app-host-plot',
  templateUrl: './host-plot.component.html',
  styleUrls: ['./host-plot.component.css']
})
export class HostPlotComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
	let dataPoints = [];
	let y = 0;		
	for ( var i = 0; i < 10000; i++ ) {		  
		y += Math.round(5 + Math.random() * (-5 - 5));	
		dataPoints.push({ y: y});
	}
	let chart = new CanvasJS.Chart("chartContainer", {
		zoomEnabled: true,
		animationEnabled: true,
		exportEnabled: true,
		title: {
			text: "Processor Utilization"
		},
		subtitles:[{
			text: "subtitle"
		}],
		data: [
		{
			type: "line",                
			dataPoints: dataPoints
		}]
	});
		
	chart.render();
    }

}

