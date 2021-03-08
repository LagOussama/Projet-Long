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
  hostNumb : number
  public protocol: any;


  constructor(private networkService:NetworkService) { }


  ngOnInit(): void {
    this.getNetworkList();

    this.hostNumb = hosts.length;

    this.getProt();


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




}
