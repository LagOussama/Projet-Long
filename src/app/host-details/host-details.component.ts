import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {HostService} from "../service/host.service";
import * as CanvasJS from '../../assets/canvasjs.min';



@Component({
  selector: 'app-host-details',
  templateUrl: './host-details.component.html',
  styleUrls: ['./host-details.component.css']
})
export class HostDetailsComponent implements OnInit {

   currentHost:any;
  currentHostIP:any;

  currentinterfaces: Array<intrf>;

  constructor( private router: Router, private route: ActivatedRoute, private hostService : HostService) {

  }


  ngOnInit(): void {
    let url = this.route.snapshot.params.hostname


    this.hostService.getResource(url)
      .subscribe(data =>{
        this.currentHost = data;
        },
          err=>{
        console.log(err)

      });



    this.onPlot();
  }
  onInterfaceInfo(i){
    let url = "/host/"+i;
    this.router.navigateByUrl(url);
  }

  onPlot(){
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
interface intrf {
  HWaddr : string;
  HostInterfaceName :string
  Hostname : string
  inet4 : string
  nb_packet_i : number
}
