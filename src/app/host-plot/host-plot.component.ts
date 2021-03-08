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

  constructor(private router: Router,
              private route: ActivatedRoute,
              private hostService : HostService,
              private hdp: HostDetailsComponent) {

    this.onGetRes();
  }

   ngOnInit(): void {

   let res =  this.currentHost;


     console.log(res)



     let data  = []



     let chart = new CanvasJS.Chart("chartContainer", {
      animationEnabled: true,
      exportEnabled: true,
      title: {
        text: "Interface Use"
      },
      data: [{
        type: "column",
        dataPoints: [

        ]
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
}
