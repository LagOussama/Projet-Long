import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {Network} from "../common/network";
import {HttpClient} from "@angular/common/http";
import {map} from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class NetworkService {

  public host:string="http://localhost:8080"

  constructor(private httpClient : HttpClient) { }

  getNetwork(){
    return this.httpClient.get(this.host+"/networks");
  }

}

