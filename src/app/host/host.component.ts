import { Component, OnInit } from '@angular/core';
import {HostService} from "../service/host.service";

@Component({
  selector: 'app-host',
  templateUrl: './host.component.html',
  styleUrls: ['./host.component.css']
})
export class HostComponent implements OnInit {

  constructor(private hostService:HostService) { }

  ngOnInit(): void {
  }

}
