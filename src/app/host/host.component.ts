import { Component, OnInit } from '@angular/core';
import {HostService} from "../service/host.service";
import {Host} from "../common/host";
import {Network} from "../common/network";

import {hosts} from "../hosts"
import {Router} from "@angular/router";

@Component({
  selector: 'app-host',
  templateUrl: './host.component.html',
  styleUrls: ['./host.component.css']
})
export class HostComponent implements OnInit {

 public hosts: any;

  constructor(private router:Router, private hostService: HostService) {
  }

  ngOnInit(): void {
    this.getHostsList();
  }


  getHostsList() {

     this.hostService.getHost().subscribe(
       data => {
         this.hosts = data;
       }, error => {
         console.log(error);

       });

  }

  onHostInfo(i){
    let url = "/host/"+i;
    this.router.navigateByUrl(url);
  }


}
