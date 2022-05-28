import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { PpListComponent } from './pp-list.component';
import { PpDetailComponent } from './pp-detail.component';
import { PpService } from "./pp.service";

import { FormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
import { Routes } from "@angular/router";
import { RouterModule } from "@angular/router";

const appRoutes: Routes = [
  {path: ':pk', component: PpDetailComponent},
  {path: '', component: PpListComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    PpListComponent,
    PpDetailComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [PpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
