import { Component, OnInit } from '@angular/core';
import {PpService} from "./pp.service";

@Component({
  selector: 'app-pp-list',
  templateUrl: './pp-list.component.html',
  styleUrls: ['./pp-list.component.css']
})
export class PpListComponent implements OnInit {
  private pps: Object[] | undefined;

  constructor(private pp_service: PpService) {}

  ngOnInit(): void {
    this.pp_service.getPps().subscribe(
      (pps: Object[]) => {this.pps = pps;}
    );
  }

}
