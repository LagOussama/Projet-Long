import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {hosts} from "../hosts";

@Component({
  selector: 'app-interface',
  templateUrl: './interface.component.html',
  styleUrls: ['./interface.component.css']
})
export class InterfaceComponent implements OnInit {

  interfaceDetail;

  constructor(  private route: ActivatedRoute) { }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    const productIdFromRoute = Number(routeParams.get('hostId'));

    this.interfaceDetail = hosts.find(hostDetail => interfaceDetail.id === productIdFromRoute);

  }

}
