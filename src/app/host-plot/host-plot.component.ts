import {AfterViewInit, Component, Input, OnInit} from '@angular/core';
import * as CanvasJS from '../../assets/canvasjs.min';
import {HostDetailsComponent} from "../host-details/host-details.component";
import {HostDetailToPlotService} from "../service/host-detail-to-plot.service";
import {ActivatedRoute, Router} from "@angular/router";
import {HostService} from "../service/host.service";


@Component({
  selector: 'app-host-plot',
  templateUrl: './host-plot.component.html',
  styleUrls: ['./host-plot.component.css']
})
export class HostPlotComponent implements OnInit {

  currentHost : any;

  @Input() Message : any



  constructor(private router: Router,
              private route: ActivatedRoute,
              private hostService : HostService,
              private hdp: HostDetailsComponent) {}

   ngOnInit(): void {


     let dataPoints = [];
     console.log("11111")


      this.currentHost = this.Message;

     console.log(this.Message.result[0].interfaces.length);


     let y = 0;
      for ( var i = 0; i < this.Message.result[0].interfaces.length; i++ ) {

        dataPoints.push({ label: this.Message.result[0].interfaces[i].HostInterfaceName, y: Number(this.Message.result[0].interfaces[i].nb_packet_i)});
      }

     let chart = new CanvasJS.Chart("chartContainer", {
       animationEnabled: true,
       exportEnabled: true,
       title: {
         text: "Interface Use"
       },
       data: [{
         type: "column",
         dataPoints: dataPoints
       }]
     });
     chart.render();

   }

   onGetRes(){
    let url = this.route.snapshot.params.hostname



     this.hostService.getResource(url)
      .subscribe(data =>{
          this.currentHost = data;

        },
        err=>{
          console.log(err)

        });
  }

}

interface intrf {
  HWaddr : string;
  HostInterfaceName :string
  Hostname : string
  inet4 : string
  nb_packet_i : number
  state : string
}

interface hostDet{
  intf : []
  ip_address : string
  name : string
  nb_packet : number

}

