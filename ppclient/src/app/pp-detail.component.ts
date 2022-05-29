import { Component, OnInit } from '@angular/core';
import {PpService} from "./pp.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-pp-detail',
  templateUrl: './pp-detail.component.html',
  styleUrls: ['./pp-detail.component.css']
})
export class PpDetailComponent implements OnInit {
  public pp: any;
  public comments: any[] | undefined;

  public author: String = '';
  public password: String = '';
  public content: String = '';

  constructor(private pp_service: PpService, private ar: ActivatedRoute) { }

  ngOnInit(): void {
    const pk = this.ar.snapshot.params['pk'];
    this.pp_service.getPp(pk).subscribe(
      (pp: Object) => {
        this.pp = pp;
        this.getComments();
      });
  }

  getComments(): void {
    this.pp_service.getComments(this.pp.id).subscribe(
      (comments: Object[]) => {this.comments = comments;}
    );
  }

  submitComment(): void {
    this.pp_service.addComment(this.pp.id, this.author, this.password, this.content)
      .subscribe(
        (comment: Object) => {
          if (comment) {
            this.content = '';
            this.getComments();
          }
        });
  }
}
