import { Component, OnInit } from '@angular/core';
import {HostService} from "../service/host.service";
import {Host} from "../common/host";
import {Network} from "../common/network";

@Component({
  selector: 'app-host',
  templateUrl: './host.component.html',
  styleUrls: ['./host.component.css']
})
export class HostComponent implements OnInit {

  hosts: Array<Host> = []

  constructor(private hostService: HostService) {
  }

  ngOnInit(): void {
    this.getHostsList();
  }

  getHostsList() {
    let host = new Host();
    host.addrIp = "192.168.1.2"
    host.adrMac = "MDh312:1e1ij:12NDau"
    host.hostName = "Host1"
    host.interfaces = ['Int1', 'Int2'];
    host.nbPaquet = 200;
    host.ports = ['Port1', 'Port2']

    this.hosts.push(host)
    console.log(host);

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
