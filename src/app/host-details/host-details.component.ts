import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {HostService} from "../service/host.service";
import * as CanvasJS from '../../assets/canvasjs.min';
import {HostDetailToPlotService} from "../service/host-detail-to-plot.service";



@Component({
  selector: 'app-host-details',
  templateUrl: './host-details.component.html',
  styleUrls: ['./host-details.component.css']
})
export class HostDetailsComponent implements OnInit {

  currentHost:any;
  currentHostIP:any;

  currentinterfaces: Array<intrf>;

  constructor( private router: Router,
               private route: ActivatedRoute,
               private hostService : HostService,
                private data: HostDetailToPlotService
               ) {

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


  }
  onInterfaceInfo(i){
    let url = "/host/"+i;
    this.router.navigateByUrl(url);
  }

  onPlot( interf ){
    console.log(interf)


  }

  get curr(){
    return this.currentHost;
  }


}
interface intrf {
  HWaddr : string;
  HostInterfaceName :string
  Hostname : string
  inet4 : string
  nb_packet_i : number
}
