import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {HostService} from "../service/host.service";
import {Host} from "../common/host";



@Component({
  selector: 'app-host-details',
  templateUrl: './host-details.component.html',
  styleUrls: ['./host-details.component.css']
})
export class HostDetailsComponent implements OnInit {

  private currentHost:any;

  constructor( private router: Router, private route: ActivatedRoute, private hostService : HostService) {

  }


  ngOnInit(): void {
    let url = this.route.snapshot.params.hostname

    this.hostService.getResource(url)
      .subscribe(data =>{
        this.currentHost = data;
        console.log(this.currentHost)
        },
          err=>{
        console.log(err)

      })
  }


}
