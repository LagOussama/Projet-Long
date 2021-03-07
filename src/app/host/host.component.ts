import { Component, OnInit } from '@angular/core';
import {HostService} from "../service/host.service";
import {Host} from "../common/host";
import {Network} from "../common/network";

import {hosts} from "../hosts"

@Component({
  selector: 'app-host',
  templateUrl: './host.component.html',
  styleUrls: ['./host.component.css']
})
export class HostComponent implements OnInit {

  hosts: any;

  constructor(private hostService: HostService) {
  }

  ngOnInit(): void {
    this.getHostsList();
  }

  getHostsList() {
    this.hosts = hosts ;

    // this.hostService.getHost().subscribe(
    //   data => {
    //     this.hosts = data;
    //   }, error => {
    //     console.log(error);
    //
    //   });

  }

  onProductInfo(i: any) {
    this.chercherHost(i)

  }

  chercherHost(i) {
    this.hostService.getHostByKeyword(i)
      .subscribe(data=>{
        //this.hosts=data;
      }, error => {
        console.log(error);
      });


  }
}
