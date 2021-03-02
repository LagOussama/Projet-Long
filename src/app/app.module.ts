import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import {RouterModule, Routes} from "@angular/router";
import { HostComponent } from './host/host.component';

const routes:Routes = [
  {path:'index',component:IndexComponent},
  {path:'host',component:HostComponent},
  {path:'', redirectTo:'/index',pathMatch:'full'}


];
@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    HostComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
