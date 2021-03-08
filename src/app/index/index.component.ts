import { Component, OnInit } from '@angular/core';
import {NetworkService} from "../service/network.service";
import {Network} from "../common/network";
import  {hosts} from "../hosts"

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  public networks: any;
  public hostNumb : any;
  public protocol: any;
  public nbPck: any;


  constructor(private networkService:NetworkService) { }


  ngOnInit(): void {
    this.getNetworkList();

   this.getHost();

    this.getProt();

    this.getPacket();


  }

   getNetworkList() {
      this.networkService.getNetwork().subscribe(
        data => {
          this.networks = data;
        }, error => {
          console.log(error);

        });
   }

  getProt() {
    this.networkService.getByProtocol().subscribe(
      data => {
        this.protocol = data;
      }, error => {
        console.log(error);

      });
  }

  getPacket() {
    this.networkService.getNbPacket().subscribe(
      data => {
        this.nbPck = data;
      }, error => {
        console.log(error);

      });
  }


  getHost() {
    this.networkService.getNbHost().subscribe(
      data => {
        this.hostNumb = data;
      }, error => {
        console.log(error);

      });
  }

}
