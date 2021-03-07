import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import { hosts } from '../hosts';


@Component({
  selector: 'app-host-details',
  templateUrl: './host-details.component.html',
  styleUrls: ['./host-details.component.css']
})
export class HostDetailsComponent implements OnInit {

  hostDetail;
  totalPaquet: number = 0;

  constructor(  private route: ActivatedRoute) {

  }

  ngOnInit(): void {
    // First get the Host id from the current route.

    const routeParams = this.route.snapshot.paramMap;
    const productIdFromRoute = Number(routeParams.get('hostId'));

    // Find the Host that correspond with the id provided in route.
    this.hostDetail = hosts.find(hostDetail => hostDetail.id === productIdFromRoute);


    for (let i = 0 ; i < this.hostDetail.nbPaquet.length ; i++){
      this.totalPaquet = this.totalPaquet + this.hostDetail.nbPaquet[i];

    }
    console.log(this.totalPaquet);




  }

}
