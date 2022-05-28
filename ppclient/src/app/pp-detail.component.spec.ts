import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PpDetailComponent } from './pp-detail.component';

describe('PpDetailComponent', () => {
  let component: PpDetailComponent;
  let fixture: ComponentFixture<PpDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PpDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PpDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
